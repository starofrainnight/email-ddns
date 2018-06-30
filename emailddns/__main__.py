#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Console script for email-ddns."""

import click
import copy
from attrdict import AttrDict
from .emailddns import (
    send_update_email, fetch_update_email, clear_update_emails)
from .exceptions import NoEMailError, EMailFetchError


def decode_host(host_text, default_port=0):
    parts = host_text.split(':')
    host = parts[0].strip()
    if len(parts) > 1:
        port = int(parts[1].strip())
    else:
        port = default_port
    return (host, port)


@click.group()
@click.option('-s', '--smtp-host', required=True,
              help="E-Mail SMTP host with format HOST[:PORT]")
@click.option('-i', '--imap-host', required=True,
              help="E-Mail IMAP host with format HOST[:PORT]")
@click.option('-a', '--account', required=True)
@click.option('-p', '--password', required=True)
@click.pass_context
def main(ctx, **kwargs):
    """Console script for email-ddns."""
    ctx.obj = kwargs

    host, port = decode_host(kwargs["smtp_host"])
    ctx.obj["smtp_host"] = host
    ctx.obj["smtp_port"] = port

    host, port = decode_host(kwargs["imap_host"])
    ctx.obj["imap_host"] = host
    ctx.obj["imap_port"] = port


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
            kwargs.imap_host, kwargs.imap_port,
            kwargs.account, kwargs.password)
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

    send_update_email(kwargs.smtp_host, kwargs.smtp_port,
                      kwargs.account, kwargs.password)

    clear_update_emails(kwargs.imap_host, kwargs.imap_port,
                        kwargs.account, kwargs.password)


if __name__ == "__main__":
    main()
