
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # registers the 3D projection

def evaluate(i, b, p):
    emvbob = 12000 + b
    emvVanessa = 14000
    emvrecruitment = 11580 + i
    emvB = p * emvVanessa + (1 - p) * emvrecruitment
    # Return 1 if the expected value of rejecting Bob is higher, otherwise 0
        # Compare Bob vs combined branch
    if emvbob >= emvB:
        return 0
    # Bob rejected: choose between Vanessa vs recruitment
    if emvVanessa >= emvrecruitment:
        return 1
    else:
        return 2

def main():
    # Define sampling ranges for each parameter
    i_vals = np.linspace(0, 800, num=20)    # salary improvement
    b_vals = np.linspace(0, 100, num=20)    # cost
    p_vals = np.linspace(0.0, 1.0, num=50)   # probability

    # Create a 3D grid of (i, b, p) triples  # 20 samples from 0.0 to 1.0
    I, B, P = np.meshgrid(i_vals, b_vals, p_vals, indexing='ij')
    I_flat = I.ravel()
    B_flat = B.ravel()
    P_flat = P.ravel()

    decisions = np.empty_like(I_flat, dtype=int)
    for idx, (i, b, p) in enumerate(zip(I_flat, B_flat, P_flat)):
        decisions[idx] = evaluate(i, b, p)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    sc = ax.scatter(
        I_flat, B_flat, P_flat,
        c=decisions,
        cmap='coolwarm',
               s=20,
        alpha=0.6
    )
    ax.set_xlabel('i (Salary Improvement)')
    ax.set_ylabel('b (Cost)')
    ax.set_zlabel('p (Probability)')
    plt.colorbar(sc, label='Decision (0=Bob, 1=Vanessa, 2=Recruitment)')
    plt.title('Decision Boundary in (i, b, p)-space')
    plt.show()


if __name__ == '__main__':
    main()



