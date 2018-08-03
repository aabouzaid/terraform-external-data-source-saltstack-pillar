#
# Example of pillar_reader.py
# A Python script to read from SaltStack Pillar, and return the value in Terraform as external data source.
#
# More info: Terraform External Data Source.
# https://www.terraform.io/docs/providers/external/data_source.html
#

# Get data from SaltStack Pillar.
data "external" "pillar" {
  program = ["python", "${path.module}/pillar_reader.py"]
  query = {
    pillar = "foo:bar"
  }
}

# You can even make it a bit shorter.
locals {
  foo_bar = "${data.external.pillar.result}"
}

# Also use it as output if you want.
output "foo_bar" {
  value = "${local.foo_bar}"
}
