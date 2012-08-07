@Homebrew()
{| cellspacing="0" cellpadding="0" class="toccolours author"
|+ This homebrew work was @if(%adopter, adopted, created) by
|-
! colspan="2" class="user" |[[Author::%authorName| ]]@if(%adopter, [[Adopter::%adopter| ]]) @if(%isnotuser, 
	@if(%adopter,
		@if(%url,
			@if(%displayName, [%url %displayName], [%url %adopter])
			@if(%displayName, %displayName, %adopter)
			),
		@if(%url,
			@if(%displayName, [%url %displayName], [%url %authorName]),
			@if(%displayName, %displayName, %authorName)
			)
		)
	)
	@if(%adopter,
		@if(%url,
			@if(%displayName, [%url %displayName], [%url %adopter]) ([[User talk:%adopter|talk]]),
			[[User:%adopter|@if(%displayName, %displayName, %adopter)]] ([[User talk:%adopter|talk]])
			),
		@if(%url,
			"@if(%displayName, [%url %displayName], [%url %authorName]) ([[User talk:%authorName|talk]])",
			"[[User:%authorName|@if(%displayName, %displayName, %authorName)]] ([[User talk:%authorName|talk]])"
			)
		)
	)
@if(%adopter,
	|-
	! Original Creator:
	| %authorName
)
|-
@if(%co-authors,
	|-
	! Co-Authors:
	| @split(%co-authors, ",", [[User:%|%]][[Author::%| ]])
)
@if(%contributors,
	|-
	! Contributors:
	| @split(%contributors, ",", %)
)
|-
	! Date Created:
	| %date_created
@if(%adopter, @if(%date_adopted,
	|-
	! Date Adopted:
	| %date_adopted
}
|-
	! Status:
	| %status
|-
	! Editing:
@if(%editing|
  | %editing|
  | [[Dungeons and Dragons Wiki:Editing Policy|Clarity edits]] only please
)
|-
@if(%balance(
	|-
	! Balance: 
	| @switch(%balance,
		Monk=[[Dungeons and Dragons_Wiki:Balance Points#Monk Level|Monk]][[Balance Point::Monk| ]],
		Fighter=[[Dungeons and Dragons Wiki:Balance Points#Fighter Level|Fighter]][[Balance Point::Fighter| ]],
		Rogue=[[Dungeons and Dragons Wiki:Balance Points#Rogue Level|Rogue]][[Balance Point::Rogue| ]],
		Wizard=[[Dungeons and Dragons Wiki:Balance Points#Wizard Level|Wizard]][[Balance Point::Wizard| ]],
                Unquantifiable=[[Dungeons and Dragons Wiki:Balance Points#Unquantifiable|Unquantifiable]][[Balance Point::Unquantifiable| ]],
 		Article is not balanced per wiki [[Dungeons_and_Dragons_Wiki:Balance_Points|guidelines]][[Balance Point::None Assigned| ]],
	)
)
|-

@if(%rating,
	|-
	! Rating: 
	| @ifexpr(%rating>=4, This article is a [[Project:Rating Articles|Community Favorite]]![[Rating::Favorite| ]][[Category:Community Favorite]], @if(%rating>0, Most [[Project:Rating Articles|raters]] like this article![[Rating::Liked| ]], @if(%rating=0, [[Project:Rating Articles|Raters]] equally like and dislike this article.[[Rating::Neither| ]], @if(%rating>-4, Most [[Project:Rating Articles|raters]] dislike this article.[[Rating::Disliked| ]], The community is generally opposed to this article as written[[Project:Deletion Policy#Community Opposed Articles|<big>*</big>]].[[Rating::Opposed| ]][[Category:Community Opposed]]))))<br />Check the [[@NAMESPACE()_Talk:@pagename()|talk page]] to see what they're saying!
,
	|-
	| colspan="2" style="text-align:center;" | <!-- Problems :\ -->

)
@if(%img,
	|- 
	| colspan="2" style="text-align:center;" |  
	|-
	| colspan="2" style="text-align:center;" | [[Image:%img|%imgsize|200px]]
	@if(%caption,
		|-
		| colspan="2" | %caption
	)
	
)
|}@if(%raters, <span style="display:none">@split(%raters, ',', [[Rated By::%]])</span>)@Pagedata()
