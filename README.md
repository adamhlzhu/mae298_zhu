# mae298_team_A
## Using UV

Purpose:
We use uv to create and manage a per-project virtual environment with pinned dependencies. This keeps everyone on the same package versions and avoids conflicts.

Steps:
1. Install uv
Follow the official instructions:
https://docs.astral.sh/uv/getting-started/installation/

2. Initialize the project (only needed once)
uv init
(You can skip this if the repo is already initialized.)

3. Create/sync the environment from pyproject.toml
uv sync
This will create .venv and install all dependencies.

4. Run commands inside the environment
uv run python --version
uv run python your_script.py

5. Add a new package to the project
uv add PACKAGE_NAME
(This updates pyproject.toml and the lockfile, then installs.)
Always commit both pyproject.toml and uv.lock after adding a new package.

6. Inspect dependencies
uv tree

Note: Added "[tool.uv.sources] -/ aviary = {path = "Aviary"}" to the "pyproject.toml" to correctly get the "toml" from Aviary file.

## Working folder
Each branch contains a working folder corresponding to its subsystem. Please write your code and data within the working folder for the part you are responsible for. This structure will make it easier to merge branches into main later and should simplify integrating all subsystems in the future.