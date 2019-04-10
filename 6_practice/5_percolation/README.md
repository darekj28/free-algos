# Percolation

## Description
__Percolation.__ Given a composite systems comprised of randomly distributed insulating and metallic materials: what fraction of the materials need to be metallic so that the composite system is an electrical conductor? Given a porous landscape with water on the surface (or oil below), under what conditions will the water be able to drain through to the bottom (or the oil to gush through to the surface)? Scientists have defined an abstract process known as percolation to model such situations.

__The model.__ We model a percolation system using an N-by-N grid of sites. Each site is either open or blocked. A full site is an open site that can be connected to an open site in the top row via a chain of neighboring (left, right, up, down) open sites. We say the system percolates if there is a full site in the bottom row. In other words, a system percolates if we fill all open sites connected to the top row and that process fills some open site on the bottom row. (For the insulating/metallic materials example, the open sites correspond to metallic materials, so that a system that percolates has a metallic path from top to bottom, with full sites conducting. For the porous substance example, the open sites correspond to empty space through which water might flow, so that a system that percolates lets water fill open sites, flowing from top to bottom.)

![percolates](percolates.png)

__The problem.__ In a famous scientific problem, researchers are interested in the following question: if sites are independently set to be open with probability p (and therefore blocked with probability 1 − p), what is the probability that the system percolates? When p equals 0, the system does not percolate; when p equals 1, the system percolates. The plots below show the site vacancy probability p versus the percolation probability for 20-by-20 random grid (left) and 100-by-100 random grid (right).

![percolation-threshold20](percolation-threshold20.png)

When N is sufficiently large, there is a threshold value p* such that when p < p* a random N-by-N grid almost never percolates, and when p > p*, a random N-by-N grid almost always percolates. No mathematical solution for determining the percolation threshold p* has yet been derived. Your task is to write a computer program to estimate p*.


## Part 1 - Model a Percolation System
Create a data type Percolation with the following API. 

```
class Percolation:
    # create N-by-N grid, with all sites blocked
    def __init__(self):

    # open site (row i, column j) if it is not already
    def open(self, i, j):

    # is site (row i, column j) open?
    def isOpen(self, i , j):

    # is site (row i, column j) full?
    def isFull(self, i, j):

    # does the system percolate?
    def percolate(self):
```

By convention, the indices i and j are integers between 0 and N − 1, where (0, 0) is the upper-left site: Raise an exception if either `i` or `j` is outside this range. The constructor should take time proportional to N^2; all methods should take constant time plus a constant number of calls to the union-find methods `union()`, `find()`, `connected()`, and `count()`. 

To assist you in this problem use [WeightedQuickUnionUF](weighted_quick_union_uf.py) in percolation.py.


## Part 2 - Percolation Stats
__Monte Carlo simulation.__ To estimate the percolation threshold, consider the following computational experiment:

- Initialize all sites to be blocked.
- Repeat the following until the system percolates:
    - Choose a site (row i, column j) uniformly at random among all blocked sites.
    - Open the site (row i, column j).
- The fraction of sites that are opened when the system percolates provides an estimate of the percolation threshold.

For example, if sites are opened in a 20-by-20 lattice according to the snapshots below, then our estimate of the percolation threshold is 204/400 = 0.51 because the system percolates when the 204th site is opened.

![percolation-150](percolation-150.png)

By repeating this computation experiment T times and averaging the results, we obtain a more accurate estimate of the percolation threshold. Let xt be the fraction of open sites in computational experiment t. The sample mean μ provides an estimate of the percolation threshold; the sample standard deviation σ measures the sharpness of the threshold.

![percolation-stats](percolation-stats.png)

Assuming T is sufficiently large (say, at least 30), the following provides a 95% confidence interval for the percolation threshold:

![percolation-confidence](percolation-confidence.png)

In order to perform a series of computational experiments, create a data type PercolationStats with the following API.

```
class PercolationStats:
   def __init__(self, N, T):    # perform T independent computational experiments on an N-by-N grid
   def mean(self):                     # sample mean of percolation threshold
   def stddev(self):                   # sample standard deviation of percolation threshold
   def confidenceLow(self):            # low end of 95% confidence interval
   def confidenceHigh(self):           # high end of 95% confidence interval 
```

The constructor should throw an exception if either `N ≤ 0` or `T ≤ 0`.

The constructor should take two arguments N and T, and perform T independent computational experiments (discussed above) on an N-by- N grid. Using this experimental data, it should calculate the mean, standard deviation, and the 95% confidence interval for the percolation threshold. Use Python's random library to generate random numbers; use Python's statistics library from to compute the sample mean and standard deviation.

## Testing
To check your code simply run 

```
python test_percolation.py
```

