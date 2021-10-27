import java.util.ArrayList;
import java.util.List;

public class LowestCommonAncestor {
	Node root;
	private List<Integer> firstPath = new ArrayList<>();
	private List<Integer> secondPath = new ArrayList<>();

	// Finds the path from root node to given root of the tree.
	int findLCA(int n1, int n2) {
		clearPaths();
		return findLCAInternal(root, n1, n2);
	}

	// Clears both paths (Array-Lists) for both of the nodes in question.
	 void clearPaths() {
		firstPath.clear();
		secondPath.clear();
	}

	// Private helper function for findLCA(int n1, int n2) which finds the lowest common ancestor.
	private int findLCAInternal(Node root, int n1, int n2) {
		if (!findPath(root, n1, firstPath) || !findPath(root, n2, secondPath)) {
			return -1;
		}
		int i;
		for (i = 0; i < firstPath.size() && i < secondPath.size(); i++) {
			if (!firstPath.get(i).equals(secondPath.get(i)))
				break;
		}
		return firstPath.get(i-1);
	}

	// Finds the path from root node to given root of the tree, Stores the
    // path in a vector path[], returns true if path exists otherwise false
	private boolean findPath(Node root, int n, List<Integer> path){
		//Base case
		if (root == null) {
			return false;
		}
		//Store this node. The node will be removed if not in path from root to n.
		path.add(root.data);
		if (root.data == n) {
			return true;
		}
		if (root.left != null && findPath(root.left, n, path)) {
			return true;
		}
		if (root.right != null && findPath(root.right, n, path)) {
			return true;
		}
		//If not present in subtree rooted with root, remove root from path[] and return false
		path.remove(path.size()-1);
		return false;
	}
}