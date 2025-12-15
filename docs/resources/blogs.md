---
tags:
  - blogs
---

{% set data = load_page_yaml("blogs.yaml") %}

# Blogs & Newsletters

## Companies

<table>
  <thead>
    <tr>
      <th>Name &amp; link</th>
      <th>Category</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    {% for blog in data.companies | sort(attribute="name") %}
    <tr>
      <td><a href="{{ blog.url }}">{{ blog.name }}</a></td>
      <td>{{ blog.category }}</td>
      <td>{{ blog.notes }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

## People

- [Alex Ewerlöf](https://blog.alexewerlof.com/)
- [The Owl and the Beetle by Luca Sartoni](https://www.theowlandthebeetle.email/)
- [Hagakure by Paulo André](https://hagakure.substack.com/)
- [Level Up Software Engineering by Caleb Mellas](https://levelupsoftwareengineering.substack.com/)
- [Journal of Discoveries by Roberto Ferraro](https://robertoferraro.substack.com/)
- [The Engineering Leader by Rafa Páez](https://newsletter.rafapaez.com/)
- [The Conscious Leader by Taha Hussain](https://tahahussain.substack.com/)
