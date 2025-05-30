# Use a Python image with uv pre-installed
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Install the project into `/app`
WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

# Install the project's dependencies using the lockfile and settings
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

# Then, add the rest of the project source code and install it
ADD . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Reset the entrypoint, don't invoke `uv`
ENTRYPOINT []

# Install NodeJS
RUN apt update && apt install -y npm 
#RUN npx @modelcontextprotocol/inspector
RUN echo node_version=$(node -v) 
RUN npm i @modelcontextprotocol/inspector@0.11.0
#RUN CLIENT_PORT=8081 SERVER_PORT=9000 npx @modelcontextprotocol/inspector 

EXPOSE 6274
EXPOSE 6277

#EXPOSE 8081
#EXPOSE 9000

# Run the FastAPI application by default
#CMD ["mcp", "run","server-1.py"] #v1.0.1
CMD ["npx" ,"@modelcontextprotocol/inspector"]
