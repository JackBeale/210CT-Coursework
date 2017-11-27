// task6BinarySearch.cpp : Defines the entry point for the console application.
#include "iostream"
using namespace std;
bool J = false;
	class BinTreeNode {
	public:
		BinTreeNode(int value) {
			this->value = value;
			this->left = NULL;
			this->right = NULL;
		}
		int value;
		BinTreeNode* left;
		BinTreeNode* right;
	};
	BinTreeNode* tree_insert(BinTreeNode* tree, int item) {
		if (tree == NULL)
			tree = new BinTreeNode(item);
		else
			if (item < tree->value)
				if (tree->left == NULL)
					tree->left = new BinTreeNode(item);
				else
					tree_insert(tree->left, item);
			else
				if (tree->right == NULL)
					tree->right = new BinTreeNode(item);
				else
					tree_insert(tree->right, item);
		return tree;
	}
	void postorder(BinTreeNode* tree) {
		if (tree->left != NULL)
			postorder(tree->left);
		if (tree->right != NULL)
			postorder(tree->right);
            cout << tree->value<<endl;
	}
	void in_order(BinTreeNode* tree) {
		if (tree->left != NULL)
			in_order(tree->left);
            cout << tree->value<<endl;
		if (tree->right != NULL)
			in_order(tree->right);
	}
	BinTreeNode * FINDMIN(BinTreeNode*tree)
	{
		while (tree->left != NULL)
		{
			tree = tree->left;
		}
		return tree;
	}
	bool Search(BinTreeNode*tree, int item) {
		if (tree == NULL) {
			return false;
		}
		else if (tree->value == item)
		{
			return true;
		}
		else if (item < tree->value) {
			Search(tree->left, item);
		}
		else if (item > tree->value)
		{
			Search(tree->right, item);
		}
	}
	BinTreeNode* Delete(BinTreeNode*tree, int item) {
		J = Search(tree, item);
			if (tree == NULL) {
				return tree;
			}
		else if (item < tree->value) {
			tree->left = Delete(tree->left, item);
		}
		else if (item > tree->value) {
			tree->right = Delete(tree->right, item);
		}
		else {
			if (tree->left == NULL &&tree->right == NULL)
			{
				delete tree;
				tree = NULL;
				return tree;
			}
			else if(tree->left==NULL){
				 BinTreeNode* temp = tree;
				tree = tree->right;
				delete temp;
				return tree;
			}
			else if (tree->right == NULL) {
				 BinTreeNode* temp = tree;
				tree = tree->left;
				delete temp;
				return tree;
			}
			else {
				 BinTreeNode*temp = FINDMIN(tree->right);
				 tree->value = temp->value;
				 tree->right = Delete(tree->right, temp->value);
			}
		}
		return tree;
	}
	int main(int argc, char *argv[])
	{
		BinTreeNode* t = tree_insert(0, 6);
		tree_insert(t, 10);
		tree_insert(t, 5);
		tree_insert(t, 2);
		tree_insert(t, 3);
		tree_insert(t, 4);
		tree_insert(t, 11);
		postorder(t);
		cout << "After Deletion:"<<endl;
		Delete(t, 5);
		postorder(t);
		return 0;
	}
	//Refferance the bellow website for the code, which i have editied to match Dianas:
