import click


def validate_pdb2pqr(ctx, param, value):
    if ctx.params.get("cmd_history"):
        return value
    if value:
        if len(value) != 1:
            raise click.BadParameter(
                "pdb2pqr requires exactly one arguments: <pdb_filepath>.pdb."
            )
        if not (value[0].endswith(".pdb")):
            raise click.BadParameter("The first argument must be a .pdb file.")
    return value


def validate_apbs(ctx, param, value):
    if ctx.params.get("cmd_history"):
        return value
    if value:
        if len(value) != 1 or not value[0].endswith(".in"):
            raise click.BadParameter(
                "apbs requires exactly one argument with .in file type."
            )
    return value


def validate_dx(ctx, param, value):
    if value:
        if not value.endswith(".dx"):
            raise click.BadParameter(
                "Output generations requires exactly one argument with .dx file type."
            )
    return value


def validate_pqr(ctx, param, value):
    if value:
        if not value.endswith(".pqr"):
            raise click.BadParameter(
                "Output generations requires exactly one argument with .pqr file type."
            )
    return value


def validate_into(ctx, param, value):
    if value:
        if not value.endswith(".in"):
            raise click.BadParameter(
                "apbs requires exactly one argument with .in file type."
            )
    return value


def validate_toin(ctx, param, value):
    if value:
        if not value.endswith(".toml"):
            raise click.BadParameter(
                "apbs requires exactly one argument with .toml file type."
            )
    return value
