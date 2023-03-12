# -*- coding: utf-8 -*-
from lxml import etree
# In Odoo, the etree module is commonly used to manipulate the view definitions, 
# which are defined in XML format, 
# and to modify the content of reports or data files that are stored in XML format.

from odoo import models, fields, api

class Product_template(models.Model):
    _inherit = "product.template"
    
    size_box = fields.Float('Size Box')
    
    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        # OVERRIDE to add the 'available_partner_bank_ids' field dynamically inside the view.
        # TO BE REMOVED IN MASTER
        res = super().fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        # first we add a condition to know if we ar in an form view
        if view_type == 'form':
            doc = etree.XML(res['arch'])
            # here we are trying to add a field next to company_id
            company_id = doc.xpath("//field[@name='company_id']")
            if company_id:
                size_box = etree.Element('field',name='size_box',string='Size of the box')
                
                company_id[0].addnext(size_box)
                
                # Serialize the modified XML definition and return it
                res['arch'] = etree.tostring(doc)
            
            """
                how to remove a field from a view
            """
            barcode = doc.xpath("//field[@name='barcode']")
            if barcode:
                for node in barcode:
                    node.getparent().remove(node)
                res['arch'] = etree.tostring(doc)
                
            
            
        return res