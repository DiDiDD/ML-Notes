import torch
import torch.nn as nn
from tqdm import tqdm


def test_model(model,
               device,
               best_ckpt_path,
               final_ckpt_path,
               test_loader,
               criterion):
    model.eval()
    model = model.to(device)

    assert not((best_ckpt_path is None) and (final_ckpt_path is None)), 'At least provide a checkpoint'

    best_ckpt_test_loss = 0
    test_loss_history_1 = []
    if best_ckpt_path is not None:
        model.load_state_dict(torch.load(best_ckpt_path))
        for inputs, labels in tqdm(test_loader):
            inputs, labels = inputs.to(device), labels.to(device)

            outputs = model(inputs)
            outputs = torch.sigmoid(outputs)
            loss = criterion(outputs, labels)

            best_ckpt_test_loss += loss
            test_loss_history_1.append(best_ckpt_test_loss)

        best_ckpt_test_loss /= len(test_loader)

    print(best_ckpt_test_loss)

    final_ckpt_test_loss = 0
    test_loss_history_2 = []
    if final_ckpt_path is not None:
        model.load_state_dict(torch.load(final_ckpt_path))
        for inputs, labels in tqdm(test_loader):
            inputs, labels = inputs.to(device), labels.to(device)

            outputs = model(inputs)
            loss = criterion(outputs, labels)

            final_ckpt_test_loss += loss
            test_loss_history_2.append(final_ckpt_test_loss)

        final_ckpt_test_loss /= len(test_loader)

    return


