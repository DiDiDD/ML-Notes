import argparse

'''Add ArgParser'''
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_name', type=str, required=True, choices=['LSTM', 'MLP', 'TransLSTM'],
                        help="Name of the model to be used (choices: 'LSTM', 'MLP', 'TransLSTM').")

    parser.add_argument('--input_dim', type=int, required=True, help="Dimension of the input.")
    parser.add_argument('--hidden_dim', type=int, required=True, help="Dimension of the hidden layer.")
    parser.add_argument('--output_dim', type=int, required=True, help="Dimension of the output layer.")
    parser.add_argument('--num_layers', type=int, required=True, help="Number of layers/blocks in each model.")

    parser.add_argument('--daily_data_path', type=str, required=True, help="Path to daily_data.csv")
    parser.add_argument('--hourly_data_path', type=str, required=True, help="Path to hourly_data.csv")
    parser.add_argument('--prices_data_path', type=str, required=True, help="Path to prices.csv")

    parser.add_argument('--if_train', action='store_true', default=False,  help="If train the model, if not, just test")

    parser.add_argument('--best_ckpt_path', type=str, default=None, required=True, help='')
    parser.add_argument('--final_ckpt_path', type=str, default=None,required=True, help='')
    parser.add_argument('--num_epochs', type=int, required=True, help="")

    return parser.parse_args()