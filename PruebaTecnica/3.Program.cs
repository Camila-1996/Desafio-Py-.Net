using System;

public class Node
{
    public int Value;
    public Node Left;
    public Node Right;

    public Node(int value)
    {
        Value = value;
        Left = Right = null;
    }
}

public class BinaryTree
{
    private Node root;

    public BinaryTree()
    {
        root = null;
    }

    // Método para insertar un valor en el árbol
    public void Insert(int value)
    {
        root = InsertRec(root, value);
    }

    private Node InsertRec(Node node, int value)
    {
        if (node == null) return new Node(value);

        if (value < node.Value)
            node.Left = InsertRec(node.Left, value);
        else if (value > node.Value)
            node.Right = InsertRec(node.Right, value);

        return node;
    }

    // Método para buscar un valor en el árbol
    public bool Search(int value)
    {
        return SearchRec(root, value);
    }

    private bool SearchRec(Node node, int value)
    {
        if (node == null) return false;
        if (node.Value == value) return true;

        return value < node.Value ? SearchRec(node.Left, value) : SearchRec(node.Right, value);
    }

    // Método para imprimir el árbol en orden ascendente (Inorden)
    public void InOrderTraversal()
    {
        InOrderRec(root);
        Console.WriteLine();
    }

    private void InOrderRec(Node node)
    {
        if (node != null)
        {
            InOrderRec(node.Left);
            Console.Write(node.Value + " ");
            InOrderRec(node.Right);
        }
    }
}

// Ejemplo de uso
class Program
{
    static void Main()
    {
        BinaryTree tree = new BinaryTree();

        tree.Insert(50);
        tree.Insert(30);
        tree.Insert(70);
        tree.Insert(20);
        tree.Insert(40);
        tree.Insert(60);
        tree.Insert(80);

        Console.WriteLine("Árbol en orden ascendente:");
        tree.InOrderTraversal(); // Salida: 20 30 40 50 60 70 80

        Console.WriteLine("Buscar 40: " + tree.Search(40)); // true
        Console.WriteLine("Buscar 90: " + tree.Search(90)); // false
    }
}
