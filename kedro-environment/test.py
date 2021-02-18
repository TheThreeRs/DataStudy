from kedro.pipeline import node


# Prepare first node
def return_greeting():
    return "Hello"


return_greeting_node = node(
    func=return_greeting, inputs=None, outputs="my_salutation"
)