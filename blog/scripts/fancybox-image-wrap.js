hexo.extend.filter.register('after_render:html', function(str, data) {
  if (!str) return str;
  // 在最终生成的 HTML 中包裹 <img> 为 Fancybox 链接，避免修改 markdown 渲染器
  return str.replace(/<img([^>]*)>/g, function(match, imgAttrs) {
    var srcMatch = imgAttrs.match(/src="([^"]*)"/);
    var src = srcMatch ? srcMatch[1] : '';
    var altMatch = imgAttrs.match(/alt="([^"]*)"/);
    var alt = altMatch ? altMatch[1] : '';
    // 保持 data-src 与最终 img src 一致（after_render 阶段已是最终路径）
    return '<a data-fancybox="gallery" data-src="' + src + '" data-caption="' + (alt || '') + '"><img' + imgAttrs + '></a>';
  });
});

