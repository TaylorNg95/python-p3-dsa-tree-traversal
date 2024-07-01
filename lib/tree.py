class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    result = id
    nodes_to_visit = [self.root]
    while len(nodes_to_visit) > 0:
      node = nodes_to_visit.pop()
      if node['id'] == result:
        return node
      else:
        nodes_to_visit = node['children'] + nodes_to_visit
    return None

tree = Tree(
      {
        'tag_name': 'body',
        'id': None,
        'children': [
          {
            'tag_name': 'div',
            'id': 'main',
            'children': [
              {
                'tag_name': 'h1',
                'id': 'heading',
                'text_content': 'Title',
                'children': []
              },
              {
                'tag_name': 'h2',
                'id': None,
                'text_content': 'Subitle',
                'children': []
              }
            ]
          }
        ]
      }
    )

print(tree.get_element_by_id('heading'))