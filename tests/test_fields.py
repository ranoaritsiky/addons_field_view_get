from odoo.tests.common import TransactionCase

class TestCustomModule(TransactionCase):
    def setUp(self):
        super(TestCustomModule, self).setUp()
        self.env = self.env(user=self.env.ref('base.user_admin'))
        
    def test_new_field(self):
        print('rakoto')
        record = self.env['product.template'].create({
            'name':'test product',
            'size_box': 22.2
        })
        
        self.assertEqual(record.name,'test product')
        self.assertEqual(record.size_box, 22.2)