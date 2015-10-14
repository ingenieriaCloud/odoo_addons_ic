$(document).ready(function () {
$('.oe_website_sale').each(function () {
    var oe_website_sale = this;
    var showAlerts = false;

    function price_to_str(price) {
        price = Math.round(price * 100) / 100;
        var dec = Math.round((price % 1) * 100);
        return price + (dec ? '' : '.0') + (dec%10 ? '' : '0');
    }

    $(oe_website_sale).on('change', 'input.js_variant_change_ic, select.js_variant_change_ic, ol[data-attribute_value_ids]', function (ev) {
        if(showAlerts) alert('change variant!!' + $(this));
        if(showAlerts) alert("$this ID: " + $(this).val());

        if($(this).val()){
            var $ul = $(ev.target).closest('ol.js_add_cart_variants');
            var $parent = $ul.closest('.js_product');
            var $product_id = $parent.find('input.product_id').first();
            var $price = $parent.find(".oe_price:first .oe_currency_value");
            var $default_price = $parent.find(".oe_default_price:first .oe_currency_value");
            var $optional_price = $parent.find(".oe_optional:first .oe_currency_value");
            var variant_ids = $ul.data("attribute_value_ids");
            var values = [];
            $parent.find('input.js_variant_change_ic:checked, select.js_variant_change_ic').each(function () {
                values.push(+$(this).val());
            });

            $parent.find("label").removeClass("text-muted css_not_available");

            var product_id = false;
            for (var k in variant_ids) {
                if (_.isEmpty(_.difference(variant_ids[k][1], values))) {
                    $price.html(price_to_str(variant_ids[k][2]));
                    $default_price.html(price_to_str(variant_ids[k][3]));
                    if (variant_ids[k][3]-variant_ids[k][2]>0.2) {
                        $default_price.closest('.oe_website_sale').addClass("discount");
                        $optional_price.closest('.oe_optional').show().css('text-decoration', 'line-through');
                    } else {
                        $default_price.closest('.oe_website_sale').removeClass("discount");
                        $optional_price.closest('.oe_optional').hide();
                    }
                    product_id = variant_ids[k][0];
                    break;
                }
            }
            if(showAlerts) alert("product ID:" + product_id);
            if(showAlerts) alert("$this ID: " + $(this).val());
            if (product_id) {
                var $img = $(this).closest('tr.js_product, .oe_website_sale').find('span[data-oe-model^="product."][data-oe-type="image"] img:first, img.product_detail_img');
                if(!$img || $img.length == 0){
                    $img = $(".img.img-responsive.img_set");
                }
                if(showAlerts) alert("antigua imagen:" + $img.attr("src"));
                $img.attr("src", "/website/image/product.attribute.value/"+ $(this).val()+"/image");
                //$img.attr("src", "/web/binary/image?model=product.attribute.value&field=image&id="+ $(this).val());
                $img.attr("style", "");
                $img.parent().attr('data-oe-model', 'product.attribute.value').attr('data-oe-id', $(this).val())
                    .data('oe-model', 'product.attribute.value').data('oe-id', $(this).val());

            }

            $parent.find("input.js_variant_change_ic:radio, select.js_variant_change_ic").each(function () {
                var $input = $(this);
                var id = +$input.val();
                var values = [id];

                $parent.find("ol:not(:has(input.js_variant_change_ic[value='" + id + "'])) input.js_variant_change_ic:checked, select").each(function () {
                    values.push(+$(this).val());
                });

                for (var k in variant_ids) {
                    if (!_.difference(values, variant_ids[k][1]).length) {
                        return;
                    }
                }

                if(showAlerts) alert("Cambiando producto a no disponible....");
                $input.closest("label").addClass("css_not_available");
                $input.find("option[value='" + id + "']").addClass("css_not_available");
            });

            if (product_id) {
                if(showAlerts) alert("Cambiando producto a SI disponible....");
                $parent.removeClass("css_not_available");
                $product_id.val(product_id);
                $parent.find(".js_check_product").removeAttr("disabled");
            } else {
                if(showAlerts) alert("Cambiando producto a NO disponible....");
                $parent.addClass("css_not_available");
                $product_id.val(0);
                $parent.find(".js_check_product").attr("disabled", "disabled");
            }
        }
    });

    $('ol.js_add_cart_variants', oe_website_sale).each(function () {
        $('input.js_variant_change_ic, select.js_variant_change_ic', this).first().trigger('change');
    });
});
});