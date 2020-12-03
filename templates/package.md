# [{{ package }}](https://pypi.org/project/{{ package }})
{% if package_data["requires_dist"]["dists"] %}
## Dependencies
{% for specifier in package_data["requires_dist"]["specifiers"] %}{% set dist = dist_from_requires_dist(specifier) %}- [{{ specifier }}](packages/{{ dist[0] }}/{{ dist }}.md)
{% endfor %}{% endif %}
{% if package_data["requires_extras"] %}
## Extras
{% for extra, extra_data in package_data["requires_extras"].items() %}
### {{ extra }}
{% for specifier in extra_data["specifiers"] %}{% set dist = dist_from_requires_dist(specifier) %}- [{{ specifier }}](packages/{{ dist[0] }}/{{ dist }}.md)
{% endfor %}{% endfor %}{% endif %}
{% if package_data["publishers"] %}
## Publishers
{% for publisher in package_data["publishers"] %}- [{{ publisher }}](https://pypi.org/user/{{ publisher }})
{% endfor %}{% endif %}
{% if package_data["yanked"] %}
## Yanked Versions
{% for version in package_data["yanked"] %}- [{{ version }}](https://pypi.org/project/{{ package }}/{{ version }})
{% endfor %} {% endif %}
