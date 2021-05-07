# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines


def term_show(client,
              publisher,
              product,
              plan):
    return client.get(offer_type="virtualmachine",
                      publisher_id=publisher,
                      offer_id=product,
                      plan_id=plan)
