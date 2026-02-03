from fingers_erp import calc_mean_erp

trial_points = "events_file_ordered.csv"
ecog_data = "brain_data_channel_one.csv"


fingers_erp_mean = calc_mean_erp(trial_points, ecog_data)

print(fingers_erp_mean.shape)
