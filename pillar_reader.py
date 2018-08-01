#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright: (c) 2017, Ahmed AbouZaid <http://aabouzaid.com/>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Read from SaltStack Pillar, and return the value in Terraform."""

import sys
try:
    import json
except ImportError:
    import simplejson as json
import salt.client


def pillar_reader():
    """Pillar reader

    The script reads JSON object from stdin, and get `pillar` as a key,
    then get pillar value from SaltStack and prints it on stdout.

    Please note: 
    This script is meant to run where SaltStack Pillar could be read,
    i.e SaltStack master.

    More info: Terraform External Data Source.
    https://www.terraform.io/docs/providers/external/data_source.html
    """

    # Make sure input is a valid JSON.
    input_json = sys.stdin.read()
    try:
        input_dict = json.loads(input_json)
    except ValueError as value_error:
        sys.exit(value_error)

    # Get pillar name.
    pillar_name = input_dict.get('pillar')

    # Print output only if JSON payload has 'pillar' as a key.
    if pillar_name:
        local = salt.client.Caller()
        output_dict = local.cmd('pillar.get', pillar_name)
        output_json = json.dumps(output_dict)
        sys.stdout.write(output_json)
    else:
        sys.exit('[ERROR] Expected JSON payload: \'{"pillar": "path:to:pillar:key"}\'')

pillar_reader()
