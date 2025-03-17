odoo.define('custom_sale_module.CopyWidget', function (require) {
    "use strict";

    var fieldRegistry = require('web.field_registry');
    var AbstractField = require('web.AbstractField');

    var CopyWidget = AbstractField.extend({
        template: 'CopyWidget',
        events: {
            'click .copy-button': '_onCopy',
        },

        _onCopy: function () {
            navigator.clipboard.writeText(this.value || '').then(() => {
                this.$('.copy-button').text('Copied!');
                setTimeout(() => {
                    this.$('.copy-button').text('Copy');
                }, 2000);
            });
        },
    });

    fieldRegistry.add('copy_widget', CopyWidget);
});
