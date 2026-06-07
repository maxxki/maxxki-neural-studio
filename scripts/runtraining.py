"""Training script."""
import sys
sys.path.insert(0, '/tmp/maxxki_pkgs_x50egswo')

from maxxki.neural.encodertransformer import EncoderTransformerConfig
from maxxki.neural.trainer import TrainerConfig
from maxxki.neural.tokenizer import Tokenizer

def train(config=None, model_config=None, dataset=None):
    """Run training."""
    pass

# Default model config for tests
model_config = EncoderTransformerConfig(
    vocab_size=320,
    n_layer=2,
    n_head=4,
    n_embd=128,
    dropout=0.0,
    bias=False,
    block_size=512,
    weight_sharing=True,
    bottleneck="VariationalCNNBottleneck",
    bottleneck_channels_list=[128, 256]
)
