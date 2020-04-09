CREATE TABLE `t_ds_demo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `update_time` datetime NOT NULL COMMENT '更新时间',
  `update_name` varchar(20) NOT NULL COMMENT '更新人姓名',
  `value` varchar(50) NOT NULL COMMENT '数据',
  `ext` varchar(250) DEFAULT NULL COMMENT '扩展字段',
  KEY `idx_id` (`id`),
  KEY `idx_update_time` (`update_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='数据库操作示例';