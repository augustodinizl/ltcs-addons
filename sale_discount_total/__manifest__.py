# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


{  # pylint: disable=C8101,C8103
    'name': "Desconto total",

    'summary': """
        Aplica desconto sobre o total da venda.""",

    'description': """
        Desconto sobre o total da venda, o desconto pode ser do tipo
        percentual ou uma quantia específica para ser descontada do
        total bruto da venda.
        Inspirado no módulo: https://github.com/CybroOdoo/CybroAddons/tree/12.0/sale_discount_total
        Com ajustes para solução de dízima gerada no rateio do desconto total em montante monetário para mais de 2 itens na sale.order.line
    """,
    'author': "LTCS",
    'website': "http://www.ltcs.com.br",
    'category': 'Uncategorized',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'contributors': [],
    'depends': ['sale'],
    'data': [
        'views/sale_order_view.xml'
    ],
}
