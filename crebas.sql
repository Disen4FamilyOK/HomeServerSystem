/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2020/2/17 16:46:15                           */
/*==============================================================*/


drop table if exists t_appuser;

drop table if exists t_order;

/*==============================================================*/
/* Table: t_appuser                                             */
/*==============================================================*/
create table t_appuser
(
   user_id              int not null,
   name                 varchar(20),
   phone                varchar(20),
   primary key (user_id)
);

/*==============================================================*/
/* Table: t_order                                               */
/*==============================================================*/
create table t_order
(
   order_id             int not null,
   user_id              int,
   title                varchar(20),
   primary key (order_id)
);

alter table t_order add constraint FK_Reference_1 foreign key (user_id)
      references t_appuser (user_id) on delete restrict on update restrict;

