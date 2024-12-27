id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
estate_access,Estate Property Access,estate.model_estate_property,base.group_user,1,1,1,1
estate_property_type_access,Estate Property Type Access,estate.model_estate_property_types,base.group_user,1,1,1,1
estate_property_tags_acesss,Estate Property Tags Access,estate.model_estate_property_tags,base.group_user,1,1,1,1

<!-- 
id: Unique identifier for the access rule (estate_access).
name: Descriptive name of the rule (Estate Property Access).
model_id:id: Target model for the access rule (estate.model_estate_property). here "estate." is name fo my module "model_" is just convetion prefix because of "model_id:id" and "estate_property" is actual model name
group_id:id: User group this rule applies to (base.group_user).
perm_read: Permission to read records (1 = allowed).
perm_write: Permission to write records (1 = allowed).
perm_create: Permission to create records (1 = allowed).
perm_unlink: Permission to delete records (1 = allowed). 
-->