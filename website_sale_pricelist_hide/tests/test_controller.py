# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import mock
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

    @mock.patch('%s.request' % imp_core)
    @mock.patch('%s.http' % imp_main)
    def test_get_search_domain_context(self, local_mk, core_mk):
        """Test extend search domain with the context pricelist"""
        core_mk.website.sale_product_domain.return_value = []
        local_mk.request.env.context.__getitem__.return_value = \
            self.pricelist_id.id

        expect = ('item_ids.pricelist_id', '=', self.pricelist_id.id)
        result = self.controller._get_search_domain(None, None, None)

        self.assertIn(
            expect,
            result,
            'Did not find pricelist in domain. Expect %s to be in %s' % (
                expect, result,
            )
        )

    @mock.patch('%s.request' % imp_core)
    @mock.patch('%s.http' % imp_main)
    def test_get_search_domain_no_context(self, local_mk, core_mk):
        """Test extend search domain with the default pricelist"""
        core_mk.website.sale_product_domain.return_value = []
        core_mk.website.get_current_pricelist.return_value = self.pricelist_id
        local_mk.request.env.context.get.return_value = False

        expect = ('item_ids.pricelist_id', '=', self.pricelist_id.id)
        result = self.controller._get_search_domain(None, None, None)

        self.assertIn(
            expect,
            result,
            'Did not find pricelist in domain. Expect %s to be in %s' % (
                expect, result,
            )
        )
