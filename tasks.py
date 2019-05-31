from invoke import task


@task(aliases=["t"])
def test(c):
    c.run("pytest")


def black(c, check):
    cmd = f"black . --line-length=79 {'--check' if check is True else ''}"
    return c.run(cmd)


@task(aliases=["f"])
def format(c):
    return black(c, False)


@task(aliases=["fc"])
def format_check(c):
    return black(c, True)


@task(aliases=["ly"])
def lint_yaml(c):
    return c.run("yamllint .")


@task(aliases=["lp"])
def lint_python(c):
    return c.run("pycodestyle .")
