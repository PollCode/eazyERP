# syntax=docker/dockerfile:1.7

# ==========================================================
# Stage 1: build — instala dependencias en un venv aislado
# ==========================================================
FROM python:3.13-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never \
    UV_HTTP_TIMEOUT=600 \
    UV_HTTP_RETRIES=20

WORKDIR /app

COPY apps/api/pyproject.toml apps/api/uv.lock ./

# Cache mount: las wheels descargadas se persisten entre builds.
# Si un build falla a mitad, el siguiente reusa lo ya bajado.
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --no-install-project

# ==========================================================
# Stage 2: runtime — imagen final mínima
# ==========================================================
FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Usuario no-root: Render lo recomienda y evita warnings
RUN useradd --create-home --uid 1000 app

WORKDIR /app

# Copiamos el venv ya resuelto del builder
COPY --from=builder --chown=app:app /app/.venv /app/.venv

# Copiamos el código del backend
COPY --chown=app:app apps/api/src ./src
COPY --chown=app:app apps/api/alembic ./alembic
COPY --chown=app:app apps/api/alembic.ini ./

# El import root es src/ (convención del proyecto)
ENV PYTHONPATH=/app/src \
    PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

USER app

EXPOSE 8000

# ${PORT:-8000}: Render inyecta $PORT en runtime.
# Si no está definido (local), usa 8000.
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000} --proxy-headers --forwarded-allow-ips='*'"]