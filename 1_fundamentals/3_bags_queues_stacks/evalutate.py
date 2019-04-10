from stack import Stack

"""
	Evaluates (fully parenthesized) arithmetic expressions using
	Dijkstra's two-stack algorithm.

	Note: the operators, operands, and parentheses must be
	separated by whitespace. Also, each operation must
	be enclosed in parentheses. For example, you must write
	( 1 + ( 2 + 3 ) ) instead of ( 1 + 2 + 3 ).

	Remarkably, Dijkstra's algorithm computes the same
	answer if we put each operator *after* its two operands
	instead of *between* them.

	input: ( 1 ( ( 2 3 + ) ( 4 5 * ) * ) + ) 
	output: 101.0

	Moreover, in such expressions, all parentheses are redundant!
	Removing them yields an expression known as a postfix expression.
	1 2 3 + 4 5 * * + 
"""
def evaluate(expression):
	ops = Stack()
	vals = Stack()
	operations = set(["+", "-", "*","/"])
	for c in expression.split(" "):
		if c in operations:
			ops.push(c)
		elif c == ")":
			op = ops.pop()
			v = vals.pop()
			if op == "+":
				v = vals.pop() + v
			elif op == "*":
				v = vals.pop() * v
			elif op == "-":
				v = vals.pop() - v
			elif op == "/":
				v = vals.pop() / v
			vals.push(v)
		elif c == "(" or c == "":
			continue
		else:
			vals.push(float(c))
	return vals.pop()

if __name__ == "__main__":
	sample_expression = "( 1 ( ( 2 3 + ) ( 4 5 * ) * ) + ) "
	print(evaluate(sample_expression))	


