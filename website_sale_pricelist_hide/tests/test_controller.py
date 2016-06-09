# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

# import mock
from openerp.tests.common import TransactionCase
from openerp.addons.website_sale_pricelist_hide.controllers.main import (
    WebsiteSale
)


imp_main = 'openerp.addons.website_sale_pricelist_hide.controllers.main'
imp_core = 'openerp.addons.website_sale.controllers.main'


class TestController(TransactionCase):

    def setUp(self):
        super(TestController, self).setUp()
        self.controller = WebsiteSale()
        self.pricelist_id = self.env['product.pricelist'].create({
            'name': 'Test List',
        })

    # @mock.patch('%s.http' % imp_core)
    # @mock.patch('%s.http' % imp_main)
    # def test_get_search_domain_context(self, local_mk, core_mk):
    #     """ It should extend the search domain with the context pricelist """
    #     core_mk.request.website.sale_product_domain.return_value = []
    #     local_mk.request.env.context.get.return_value = self.pricelist_id.id
    #     res = self.controller._get_search_domain(None, None, None)
    #     expect = ('item_ids.pricelist_id', '=', self.pricelist_id.id)
    #     found = False
    #     for item in res:
    #         if expect == item:
    #             found = True
    #             break
    #     self.assertTrue(
    #         found,
    #         'Did not find pricelist in domain. Expect %s to be in %s' % (
    #             expect, res,
    #         )
    #     )
    #
    # @mock.patch('%s.http.request.website' % imp_core)
    # @mock.patch('%s.http.request.env.context' % imp_main)
    # def test_get_search_domain_no_context(self, local_mk, core_mk):
    #     """ It should extend the search domain with the default pricelist """
    #     core_mk.request.website.sale_product_domain.return_value = []
    #     local_mk.request.env.context.get.return_value = False
    #     with mock.patch.object(self.controller, 'get_pricelist') as plist_mk:
    #         plist_mk.return_value = self.pricelist_id
    #         res = self.controller._get_search_domain(None, None, None)
    #         expect = ('item_ids.pricelist_id', '=', self.pricelist_id.id)
    #         found = False
    #         for item in res:
    #             if expect == item:
    #                 found = True
    #                 break
    #         self.assertTrue(
    #             found,
    #             'Did not find pricelist in domain. Expect %s to be in %s' % (
    #                 expect, res,
    #             )
    #         )
