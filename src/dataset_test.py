import unittest

import dataset


class TestDatasetandDataLoader(unittest.TestCase):

    dir_env = dict()
    dir_env["ext"] = ".png"
    dir_env["root"] = "./sample_data/"
    dir_env["train_good_dir"] = "train/good"
    dir_env["test_good_dir"] = None
    dir_env["test_bad_dir"] = None

    mvtec_dataset = dataset.MVTecDataset(is_train=True, dir_env=dir_env)
    dataloader = dataset.DataLoader(
        mvtec_dataset,
        batch_size=2,
        shuffle=True,
        drop_last=False,
    )

    def test_dataset(self):
        self.assertEqual(len(self.mvtec_dataset), 10)

    def test_dataloader(self):
        self.assertEqual(len(self.dataloader), 10)
        ret = 0
        for _ in self.dataloader:
            ret += 1
        self.assertEqual(ret, 10)
