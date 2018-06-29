#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Console script for email-ddns."""

import click
import copy
from attrdict import AttrDict
from .emailddns import send_update_email, fetch_update_email
from .exceptions import NoEMailError, EMailFetchError


@click.group()
@click.option('-h', '--host', required=True,
              help="E-Mail host with format HOST[:PORT]")
@click.option('-a', '--account', required=True)
@click.option('-p', '--password', required=True)
@click.pass_context
def main(ctx, **kwargs):
    """Console script for email-ddns."""
    ctx.obj = kwargs

    parts = kwargs["host"].split(':')
    host = parts[0].strip()
    if len(parts) > 1:
        port = int(parts[1].strip())
    else:
        port = 0

    ctx.obj["host"] = host
    ctx.obj["port"] = port


@main.command()
@click.pass_context
def client(ctx, **kwargs):
    """Email-DDNS Client
    """
    obj_copy = copy.deepcopy(ctx.obj)
    obj_copy.update(kwargs)
    kwargs = AttrDict(obj_copy)

    try:
        ip = fetch_update_email(
            kwargs.host, kwargs.port, kwargs.account, kwargs.password)
        click.echo(ip)
    except NoEMailError:
        click.echo("NOTE: No IP update e-mails!")
    except EMailFetchError:
        click.echo("ERROR: Failed to fetch e-mails!")


@main.command()
@click.pass_context
def server(ctx, **kwargs):
    """Email-DDNS Server.

    WARN: Only support SSL encrypted SMTP server.
    """
    obj_copy = copy.deepcopy(ctx.obj)
    obj_copy.update(kwargs)
    kwargs = AttrDict(obj_copy)

    send_update_email(kwargs.host, kwargs.port,
                      kwargs.account, kwargs.password)


if __name__ == "__main__":
    main()
