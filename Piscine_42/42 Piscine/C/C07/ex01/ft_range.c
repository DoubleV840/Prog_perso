/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: wberger <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/07/20 17:19:56 by wberger           #+#    #+#             */
/*   Updated: 2022/07/20 19:11:51 by wberger          ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */
#include	<stdlib.h>

int	*ft_range(int min, int max)
{
	int	i;
	int	size;
	int	*tab;

	i = 0;
	size = max - min;
	if (size < 0 || size == 0)
	{
		return (0);
	}
	tab = malloc(sizeof(*tab) * size);
	if (!tab)
		return (0);
	while (max != min)
	{
		tab[i++] = min++;
	}
	tab[i] = '\0';
	return (tab);
}
