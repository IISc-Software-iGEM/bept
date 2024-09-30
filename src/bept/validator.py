import click


def validate_pdb2pqr(ctx, param, value):
    if value:
        if not value.endswith(".pdb"):
            value = value + ".pdb"
    return value


def validate_apbs(ctx, param, value):
    if value:
        if not value.endswith(".in"):
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
