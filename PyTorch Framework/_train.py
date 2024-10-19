import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
import tensorboard
from tqdm import tqdm


def acc(predictions, targets):
    predicted_labels = (predictions > 0.5).float()

    # Calculate the number of correct predictions
    correct_predictions = (predicted_labels == targets).sum().item()

    # Calculate accuracy
    accuracy = correct_predictions / targets.numel()
    return accuracy

def train_model(model,
          train_loader,
          val_loader,
          train_criterion,
          val_criterion,
          optimizer,
          num_epochs,
          device,
          best_ckpt_path,
          final_ckpt_path):
    """
    Train a PyTorch model.

    Parameters:
    - model: The PyTorch model to be trained.
    - train_loader: DataLoader for the training data.
    - val_loader: DataLoader for the validation data.
    - criterion: Loss function.
    - optimizer: Optimizer.
    - num_epochs: Number of epochs to train for.
    - device: Device to train on (e.g., 'cuda' or 'cpu').

    Returns:
    - model: The trained model.
    - train_loss_history: List of training loss values.
    - val_loss_history: List of validation loss values.
    """

    model.to(device)

    train_loss_history = []
    val_loss_history = []
    best_val_loss = float('inf')
    best_val_loss = 0

    for epoch in tqdm(range(num_epochs)):
        model.train()
        running_loss = 0.0

        for inputs, labels in train_loader:
            # breakpoint()
            inputs, labels = inputs.to(device), labels.to(device)

            # Zero the parameter gradients
            optimizer.zero_grad()

            # Forward pass
            outputs = model(inputs)
            outputs = nn.Sigmoid()(outputs)

            loss = train_criterion(outputs, labels)

            # Backward pass and optimization
            loss.backward()
            optimizer.step()

            running_loss += loss.item()

        train_loss = running_loss / len(train_loader)
        train_loss_history.append(train_loss)

        # Validation phase
        model.eval()
        val_loss = 0.0

        with torch.no_grad():
            for inputs, labels in val_loader:
                inputs, labels = inputs.to(device), labels.to(device)

                outputs = model(inputs)
                outputs = torch.sigmoid(outputs)
                loss = val_criterion(outputs, labels)

                val_loss += loss

            val_loss /= len(val_loader)
            val_loss_history.append(val_loss)

            if val_loss > best_val_loss:
                best_val_loss = val_loss
                torch.save(model.state_dict(), best_ckpt_path)
                print(f'val_loss < best_val_loss, model saved at {best_ckpt_path}')

        print(f'Epoch [{epoch + 1}/{num_epochs}], Train Loss: {train_loss:.4f}, Val Loss: {val_loss:.4f}')

    torch.save(model.state_dict(), final_ckpt_path)
    print(f'Final model saved at {final_ckpt_path}')

    return model