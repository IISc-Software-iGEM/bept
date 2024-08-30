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
        if (
            len(value) != 2
            or not value[0].endswith(".pqr")
            or not value[1].endswith(".dx")
        ):
            raise click.BadParameter(
                "output generations requires exactly one argument with .pqr and one with .dx file type respectively."
            )
    return value
