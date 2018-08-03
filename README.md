# Terraform external data source script for SaltStack Pillar.

# Why?
SaltStack is more than configuration management tool, and in some environment it's [Pillar](https://docs.saltstack.com/en/latest/topics/tutorials/pillar.html) has a lot of data which could be needed somewhere else, e.g. Terraform!
So this Python script works as external data source and reads from SaltStack Pillar, and returns the value in Terraform as external data source.

# How to use
You can query any Pillar key from SaltStack and get the value in Terraform:

```
data "external" "pillar" {
  program = ["python", "${path.module}/pillar_reader.py"]
  query = {
    pillar = "foo:bar"
  }
}
```

A full example available in [pillar_reader.tf](pillar_reader.tf).

# Access and limitations
Actually it's not necessary to just have a single key, but also if that key has other keys under it you still can access them too, **as long as they are strings**!

So for example, if the Pillar has the following:

```
foo:
  bar:
    key01: "value01"
    key02: "value02"
    key03: "value03"
```

And based on previous external data source example if you query `foo:bar`, you can also access the keys under it:
```
${data.external.pillar.result.key01}
${data.external.pillar.result.key02}
${data.external.pillar.result.key03}
```
