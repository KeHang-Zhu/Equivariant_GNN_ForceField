# Graph Neural Network for Particle & Molecules

Machine learning force fields (MLFFs) are models designed to predict the potential energy and forces in molecular systems. The state-of-the-art ML models for this task often employ graph neural networks (GNNs) due to their ability to effectively represent and process complex molecular structures.

## Why graph?
Molecules can be naturally represented as graphs, where atoms are the nodes, and chemical bonds are the edges. Look at the example below:
![image](https://user-images.githubusercontent.com/9202783/208929605-1bcc1ae9-ecd3-47bb-8829-877c5a2dc0fb.png)

**The use of GNNs in MLFFs has several advantages:**
- Invariance to input order: Molecules can be represented by different graphs depending on the order in which the atoms are listed. GNNs are invariant to the input order of nodes, ensuring that the same molecule will produce the same output regardless of its input representation.

- Local and global information processing: GNNs can effectively process local information, such as the properties of individual atoms or bonds, as well as global information, such as overall molecular structure or long-range interactions. This ability allows GNNs to capture important features for predicting potential energy and forces in molecular systems.

## Why neural network?

First-principles methods, such as the Density Functional Theory (DFT), offer a precise representation of a system by explicitly accounting for its electrons. However, these methods suffer from poor scaling with system size ($N^3$), which restricts their practical application to relatively small systems, e.g. 100 atoms. 

But for the complex struture like the one below, DFT will be hopeless.
![image](https://user-images.githubusercontent.com/72799310/227837452-c5da7c94-2842-4d40-b3c3-c0ab060f435f.png)

