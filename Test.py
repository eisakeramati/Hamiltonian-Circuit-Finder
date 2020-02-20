# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:35:24 2020

@author: eisak
"""

from Graph import Graph
from Walk import Walk

def main():
  """
  Main test program calculates score for program.
  It first tests the getHamiltonian method on graphs in test files.
  Then tests it on randomly generated undirected simple graphs.
  """
  
  # Run test files
  dirPath = "./tests/"
  result = testInput(dirPath + "disconnected", 0)
  score = 4 - result
  print("Score so far: " + str(score))
  
  result = testInput(dirPath + "toosmall", 0)
  score += 2 - result
  print("Score so far: " + str(score))

  result = testInput(dirPath + "nohamiltonian", 0)
  score += 4 - result
  print("Score so far: " + str(score))
 
  result = testInput(dirPath + "hashamiltonian", 5)
  score += result
  print("Score so far: " + str(score))
 
  result = testInput(dirPath + "large", 6)
  score += result
  print("Score so far: " + str(score))
 
  result = testInput(dirPath + "verylarge", 5)
  score += result
  print("Score so far: " + str(score))
  
  result = testInput(dirPath + "onethousand", 1)
  score += 4*result
  print("Score so far: " + str(score) + " out of 40.")


  # Test random graphs
  # Will be added during grading
  print("\n=======  Test Random  =======\n")

  
  # Print final score   
  print("The final 10 marks will be calculated \nby running additional tests on five random graphs.")


def testInput(filename, expected):
  """
  Reads graphs from a file and tests the getHamiltonian method on these graphs.
  
  Parameters:
    str filename: path of file
    int expected: number of graphs in file which have a Hamiltonian circult
  
  Returns the number of valid Hamiltonian circuits for the graphs in the file.
  """
  print("\n=======  Test " + filename +"  =======\n")
  found = 0
  graphList = Graph.fromFile(filename)
  for graph in graphList:
    found += testOnGraph(graph)
  print("\nHamiltonian circuits expected: " + str(expected) + ", found: " + str(found))
  return found
  

def testOnGraph(graph):
  """
  Tests the getHamiltonian method for a graph.  Prints the results.
  
  Parameters:
    Graph graph: graph on which the getHamiltonian method will be tested
  
  Returns 1 if a valid Hamiltonian circuit has been found and 0 otherwise
  """
  print("Graph has " + str(graph.totalVertices())
			 + " vertices, and " + str(graph.totalEdges()) + " edges.");  
  hamiltonian = graph.getHamiltonian()
  if(hamiltonian is None):
    print("Graph has no Hamiltonian Circuit")
    return 0
  elif (isValidHamiltonian(graph,hamiltonian)):
    print("Valid Hamiltonian Circuit")
    return 1
  else:
    print("Invalid Hamiltonian Circuit")
    return 0


def isValidHamiltonian(graph, circuit):
  """
  Verifies whether a path is a valid Hamiltonian circuit for a graph.
  
  Parameters:
    Graph graph: original graph
    Walk circuit: potential Hamiltonian circuit for graph
  
  Returns True iff circuit is a valid Hamiltonian circuit for graph.
  """

  # First check if the path is a circuit
  if not circuit.isCircuit():
    print("Error: Path returned is not a circuit")
    return False

  # Then check if the circuit has the correct number of edges and vertices
  totalVertices = graph.totalVertices()
  if len(circuit) < totalVertices:
    print("Error: Some vertices have not been visited")
    return False
  if len(circuit) > totalVertices:
    print("Error: Too many edges in circuit")
    return False

  # Now check whether the circuit is a subgraph of the graph and goes through each vertex
  visited = [False]*totalVertices
  path = circuit.getVertices()
  for i in range(0,len(path)-1):
    vertex = path[i]
    if visited[vertex]:
      print("Error: Vertex " + str(vertex) + " occurs at least twice in the circuit.")
      return False
    visited[vertex] = True
    if graph.getEdgeCount(vertex,path[i+1]) == 0:
      print("Error: The original graph has no edge between " + str(vertex) + " and " + str(path[i+1]))
      return False
  
  return True

# calls main program
if __name__ == '__main__':
  main()