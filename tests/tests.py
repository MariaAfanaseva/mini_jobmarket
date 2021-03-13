import unittest
from tests.test_search_page import SearchPageTestCase
from tests.test_model_methods import ModelMethodsTestCase

if __name__ == "__main__":
    search = unittest.TestLoader().loadTestsFromModule(SearchPageTestCase)
    models = unittest.TestLoader().loadTestsFromModule(ModelMethodsTestCase)
    unittest.TextTestRunner(verbosity=2).run(search)
    unittest.TextTestRunner(verbosity=2).run(models)
