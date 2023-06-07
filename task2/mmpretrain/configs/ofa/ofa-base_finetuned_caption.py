_base_ = [
    '../_base_/datasets/coco_caption.py',
    '../_base_/default_runtime.py',
]

# model settings
model = dict(
    type='OFA',
    task='caption',
    vocab_size=59457,
    embedding_dim=768,
    encoder_cfg=dict(
        embed_images=dict(type='OFAResNet', depth=101),
        num_layers=6,
    ),
    decoder_cfg=dict(num_layers=6),
    generation_cfg=dict(use_cache=True),
    tokenizer=dict(type='OFATokenizer', name_or_path='OFA-Sys/OFA-base'),
)

# data settings
data_preprocessor = dict(
    type='MultiModalDataPreprocessor',
    mean=[127.5, 127.5, 127.5],
    std=[127.5, 127.5, 127.5],
    to_rgb=True,
)

test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='Resize', scale=(480, 480)),
    dict(type='PackInputs', meta_keys=('image_id', )),
]

train_dataloader = None
test_dataloader = dict(dataset=dict(pipeline=test_pipeline))

# schedule settings
train_cfg = None
val_cfg = dict()
test_cfg = dict()
