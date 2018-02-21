# {{ cookiecutter.project_name }}
{{ cookiecutter.project_short_description }}

# Requirements
 - docker
 - docker-compose

# Running locally
The docker-compose.yaml file is configured to volume mount the project
directory into the container to support reloading. This will need additional
setup on Windows machines.

You can use the following commands to run tasks inside the container.

| Purpose | Command |
|-------------------|
| Start container | `docker-compose up -d --build` |
| Delete container | `docker-compose rm -fs` |
| View container logs | `docker-compose logs -f` |
| Run tests in container | `docker-compose exec {{ cookiecutter.main_package_name }} bash utils/run_tests.sh` |
| Run linter in container | `docker-compose exec {{ cookiecutter.main_package_name }} bash utils/run_lint.sh` |
| Make docs in container | `docker-compose exec {{ cookiecutter.main_package_name }} bash utils/make_docs.sh` |

You can use the following commands locally but you will need the python
dependencies under `./requirements` installed.

| Purpose | Command |
|-------------------|
| Run tests | `bash utils/run_tests.sh` |
| Run linter | `bash utils/run_lint.sh` |
| Make docs | `bash utils/make_docs.sh` |
