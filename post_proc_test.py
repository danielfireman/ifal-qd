import unittest
from post_proc import extrai_diarios


class PostProcTest(unittest.TestCase):

    def test_qtd_municipios_2022_08_29(self):
        path = 'test_data/diario-completo-2022-08-29-extraido.txt'
        with open(path, "r") as in_file:
            texto_diario = in_file.read()
        self.assertEqual(33, len(extrai_diarios(
            texto_diario)))


if __name__ == '__main__':
    unittest.main()