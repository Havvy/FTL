{| class="d20 dragon monstats" cellspacing="0" @if(%width, %width="%width")
<!-- Set up the table widths. 33% per monster if 3 creatures, 50% if two. -->
@if(%monster3,
!
! style="width: 34%;" | @monster
! style="width: 33%;" | @monster2
! style="width: 33%;" | @monster3
)<!--
-->(@if(@if(%monster2, 1, 0) and not @if(%monster3, 1, 0),
!
! style="width: 50%;" {{!}} %monster
! style="width: 50%;" {{!}} %monster2
}}<!--
-->{{#ifexpr: @if(%monster||1|0}} and not @if(%monster2||1|0}} |
!
! %monster
}}
|-
<!-- Size/Type/Subtypes -->
! [[SRD:Reading Creature Entries#Size and Type|Size/Type]]:
| [[Size::%size]] @Property Link(Type, @if(%typelink, %typelink, SRD:%type Type), %type) @if(%subtypes, '(@\#arraymaptemplate(%subtypes, 3.5e Monster Classic/Subtype, \,))')<!--
-->@if(%monster2, || [[Size::%size2]] @Property Link(Type, @if(%typelink, %typelink, SRD:%type Type), %type) @if(%subtypes2, '(@\#arraymaptemplate(%subtypes2|3.5e Monster Classic/Subtype|\,))'))<!--
-->@if(%monster3, || [[Size::%size3]] @Property Link(Type, @if(%typelink, %typelink, SRD:%type Type), %type) @if(%subtypes3, '(@\#arraymaptemplate(%subtypes3|3.5e Monster Classic/Subtype|\,))'))
|-
<!-- Hit Dice and Hit Points -->
! [[SRD:Reading Creature Entries#Hit Dice|Hit Dice]]:
| %hd (%hp hp)<!--
-->@if(%monster2, '|| %hd2 (%hp2 hp)')<!--
-->@if(%monster3, '|| %hd3 (%hp3 hp)')
|-
<!-- Initiative Modifier -->
! [[SRD:Reading Creature Entries#Initiative|Initiative]]:
| %init<!--
-->@if(%monster2, || %init2)<!--
-->@if(%monster3, || %init3)
|-
<!-- Speed (ground, fly, etc.) -->
! [[SRD:Reading Creature Entries#Speed|Speed]]:
| %speed<!--
-->@if(%monster2, || %speed2)<!--
-->@if(%monster3, || %speed3)
|-
<!-- Armor Class -->
! [[SRD:Reading Creature Entries#Armor Class|Armor Class]]:
| %ac, touch %touch, [[SRD:Flat-Footed|flat-footed]] %flat<!--
-->@if(%monster2, || %ac2, touch %touch2, [[SRD:Flat-Footed|flat-footed]] %flat2)<!--
-->@if(%monster3, || %ac3, touch %touch3, [[SRD:Flat-Footed|flat-footed]] %flat3)
|-
<!-- BAB/Grapple -->
! [[SRD:Reading Creature Entries#Base Attack/Grapple|Base Attack/Grapple]]:
| %bab/%grapple<!--
-->@if(%monster2, || %bab2/%grapple2)<!--
-->@if(%monster3, || %bab3/%grapple3)
|-
<!-- Attack -->
! [[SRD:Reading Creature Entries#Attack|Attack]]:
| %at|—<!--
-->@if(%monster2, || %at2|—)<!--
-->@if(%monster3, || %at3|—)
|-
<!-- Full Attack -->
! [[SRD:Reading Creature Entries#Full Attack|Full Attack]]:
| %full_at|—<!--
-->@if(%monster2, || %full_at2|—)<!--
-->@if(%monster3, || %full_at3|—)
|-
<!-- Space/Reach -->
! [[SRD:Reading Creature Entries#Space/Reach|Space/Reach]]:
| %space/%reach<!--
-->@if(%monster2, || %space2/%reach2)<!--
-->@if(%monster3, || %space3/%reach3)
|-
<!-- Special Attacks -->
! [[SRD:Reading Creature Entries#Special Attacks and Special Qualities|Special Attacks]]:
| %sa|—<!--
-->@if(%monster2, || %sa2|—)<!--
-->@if(%monster3, || %sa3|—)
|-
<!-- Special Qualities -->
! [[SRD:Reading Creature Entries#Special Attacks and Special Qualities|Special Qualities]]:
| %sq|—<!--
-->@if(%monster2, || %sq2|—)<!--
-->@if(%monster3, || %sq3|—)
|-
<!-- Saves -->
! [[SRD:Reading Creature Entries#Saves|Saves]]:
| Fort %fort, Ref %ref, Will %will<!--
-->@if(%monster2, || Fort %fort2, Ref %ref2, Will %will2)<!--
-->@if(%monster3, || Fort %fort3, Ref %ref3, Will %will3)
|-
<!-- Abilities -->
! [[SRD:Reading Creature Entries#Abilities|Abilities]]:
| [[SRD:Strength|Str]] %str|—, [[SRD:Dexterity|Dex]] %dex|—, [[SRD:Constitution|Con]] %con|—, [[SRD:Intelligence|Int]] %int|—, [[SRD:Wisdom|Wis]] %wis|—, [[SRD:Charisma|Cha]] %cha|—<!--
-->@if(%monster2, || [[SRD:Strength|Str]] %str2|—, [[SRD:Dexterity|Dex]] %dex2|—, [[SRD:Constitution|Con]] %con2|—, [[SRD:Intelligence|Int]] %int2|—, [[SRD:Wisdom|Wis]] %wis2|—, [[SRD:Charisma|Cha]] %cha2|—)<!--
-->@if(%monster3, || [[SRD:Strength|Str]] %str3|—, [[SRD:Dexterity|Dex]] %dex3|—, [[SRD:Constitution|Con]] %con3|—, [[SRD:Intelligence|Int]] %int3|—, [[SRD:Wisdom|Wis]] %wis3|—, [[SRD:Charisma|Cha]] %cha3|—)
|-
<!-- Skills -->
! [[SRD:Reading Creature Entries#Skills|Skills]]:
| %skills|—<!--
-->@if(%monster2, || %skills2|—)<!--
-->@if(%monster3, || %skills3|—)
|-
<!-- Feats -->
! [[SRD:Reading Creature Entries#Feats|Feats]]:
| %feats|—<!--
-->@if(%monster2, || %feats2|—)<!--
-->@if(%monster3, || %feats3|—)
|- class="separator"
<!-- Environment -->
! [[SRD:Reading Creature Entries#Environment|Environment]]:
| [[Environment::%env|Any]]<!--
-->@if(%monster2, || [[Environment::%env2|Any]])<!--
-->@if(%monster3, || [[Environment::%env3|Any]])
|-
<!-- Organization -->
! [[SRD:Reading Creature Entries#Organization|Organization]]:
| %org|Any<!--
-->@if(%monster2, || %org2|Any)<!--
-->@if(%monster3, || %org3|Any)
|-
<!-- Challenge Rating -->
! [[SRD:Reading Creature Entries#Challenge Rating|Challenge Rating]]:
| [[Challenge Rating::%cr]]<!--
-->@if(%monster2, || [[Challenge Rating::%cr2]])<!--
-->@if(%monster3, || [[Challenge Rating::%cr3]])
|-
<!-- Treasure -->
! [[SRD:Reading Creature Entries#Treasure|Treasure]]:
| %treas|None<!--
-->@if(%monster2, || %treas2|None)<!--
-->@if(%monster3, || %treas3|None)
|-
<!-- Alignment -->
! [[SRD:Reading Creature Entries#Alignment|Alignment]]:
| [[Alignment::%align|Any]]<!--
-->@if(%monster2, || [[Alignment::%align2|Any]])<!--
-->@if(%monster3, || [[Alignment::%align3|Any]])
|-
<!-- Advancement -->
! [[SRD:Reading Creature Entries#Advancement|Advancement]]:
| %adv|—<!--
-->@if(%monster2, || %adv2|—)<!--
-->@if(%monster3, || %adv3|—)
|-
<!-- Level Adjustment -->
! [[SRD:Reading Creature Entries#Level Adjustment|Level Adjustment]]:
| [[Level Adjustment::%la|—]]<!--
-->@if(%monster2, || [[Level Adjustment::%la2|—]])<!--
-->@if(%monster3, || [[Level Adjustment::%la3|—]])
|}
