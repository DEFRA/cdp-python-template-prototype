# To Do
Once "hello world" is deployed and running in dev:

1. Metrics
2. Structure the app properly, as per [Fast API Guidelines](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
3. Link it to the Defra Python dev standards - example code and README
4. Testing - [Fast API Docs](https://fastapi.tiangolo.com/tutorial/testing/#testing-file). [Tox](https://tox.wiki/en/4.21.2/#). [Github Actions](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-python#running-tests-with-tox)
5. Linting - [Ruff](https://docs.astral.sh/ruff/). [Github Actions](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-python#using-ruff-to-lint-code) 
6. Other Github actions - `publish-hotfix.yml`, `example.dependabot.yml`
7. Sonar config - `sonar-project.properties`
8. A python base image (including the self-signed cert)
9. At the moment, the argument `--no-access-log` is provided in the `Dockerfile`, [as per docs](https://www.uvicorn.org/settings/#logging). A more fine-grained approach to just prevent logging access to `/health` can be implemented, [as per this](https://github.com/encode/starlette/issues/864)
