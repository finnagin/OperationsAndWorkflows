# {{ data.name }}

{% if 'subclass_of' in data -%}
_subclass of [{{ data.subclass_of }}](./{{ data.subclass_of }}.md)_
{%- endif -%}{{ data.description }}

{% if data.examples -%}
### examples

{% for example in data.examples -%}
- [input](../examples/{{ example.input }}), [output](../examples/{{ example.output }})
{% endfor %}
{% endif %}### input requirements

{% if data.input_requirements -%}
{%- for requirement in data.input_requirements -%}
- {{ requirement }}
{% endfor -%}
{%- else -%}
None
{% endif %}
### output guarantees

{% if data.output_guarantees -%}
{%- for guarantee in data.output_guarantees -%}
- {{ guarantee }}
{% endfor -%}
{%- else -%}
None
{% endif %}
### allowed changes

{% if data.allowed_changes -%}
{%- for allowed_change in data.allowed_changes -%}
- {{ allowed_change }}
{% endfor -%}
{%- endif %}
### parameters

```yaml
{{ data.parameters }}```
