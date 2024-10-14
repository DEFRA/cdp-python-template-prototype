# To Do

Initial "Hello World":

1. Logging
2. Metrics

Once "hello world" is deployed and running in dev:

1. Structure the app properly, as per [Fast API Guidelines](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
2. Link it to the Defra Python dev standards - example code and README
3. Testing - [Fast API Docs](https://fastapi.tiangolo.com/tutorial/testing/#testing-file). [Tox](https://tox.wiki/en/4.21.2/#). [Github Actions](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-python#running-tests-with-tox)
4. Linting - [Ruff](https://docs.astral.sh/ruff/). [Github Actions](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-python#using-ruff-to-lint-code) 
5. Other Github actions - `publish-hotfix.yml`, `example.dependabot.yml`
6. Sonar config - `sonar-project.properties`
7. A python base image (including the self-signed cert)
