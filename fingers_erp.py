import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def calc_mean_erp(trial_points, ecog_data):
    """
    Calculate the mean ERP for each finger movement.

    Parameters
    ----------
    trial_points : str
        Path to CSV file containing starting point, peak point, and finger number.
    ecog_data : str
        Path to CSV file containing ECoG time series data.

    Returns
    -------
    fingers_erp_mean : np.ndarray
        Matrix of shape (5, 1201) containing mean ERP for fingers 1–5.
    """

    # Load CSV files and force integer type for trial_points
    trials = pd.read_csv(trial_points).astype(int)
    brain = pd.read_csv(ecog_data).astype(int).values.flatten()

    fingers_erp_mean = np.zeros((5, 1201))

    # Loop through each finger (1 to 5)
    for finger in range(1, 6):
        finger_trials = trials[trials["finger"] == finger]

        all_trials = []

        # Extract brain signal around each movement
        for _, row in finger_trials.iterrows():
            start = row["starting_point"]
            segment = brain[start - 200 : start + 1001]
            all_trials.append(segment)

        all_trials = np.array(all_trials)

        # Average across trials
        fingers_erp_mean[finger - 1, :] = np.mean(all_trials, axis=0)

        # Plot ERP
        plt.plot(fingers_erp_mean[finger - 1], label=f"Finger {finger}")

    plt.xlabel("Time (ms)")
    plt.ylabel("Amplitude")
    plt.title("Mean ERP per Finger")
    plt.legend()
    plt.show()

    return fingers_erp_mean
